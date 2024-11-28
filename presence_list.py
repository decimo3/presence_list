''' Module that uses face recognition to validate  '''
#region imports
import os
import sys
import json
import face_recognition
from result_model import Result
#endregion imports

TOLERANCE = 0.6

# Convert the distance to a percentage accuracy
def face_distance_to_confidence(face_distance, threshold=0.6):
  ''' Function to calculate percentage between faces diference '''
  if face_distance > threshold:
    return max(0, 100 - (face_distance / threshold) * 100)
  return min(100, (1.0 - face_distance / threshold) * 100)

def compare_image_faces(imgpath_1: str, imgpath_2: str) -> float:
  ''' Function that load two images and compare to find same face '''
  # Load known image (the reference image)
  known_image = face_recognition.load_image_file(imgpath_1)
  known_faces_encoding = face_recognition.face_encodings(known_image)

  # Ensure if there are only one face in the first image
  if len(known_faces_encoding) != 1:
    return 1

  known_face_encoding = known_faces_encoding[0]

  # Load an unknown image (the image you want to compare)
  unknown_image = face_recognition.load_image_file(imgpath_2)
  # Get all encodes to images with more that one face
  unknown_faces_encoding = face_recognition.face_encodings(unknown_image)

  # Calculate the Euclidean distance between the encodings
  face_distances = face_recognition.face_distance(unknown_faces_encoding, known_face_encoding)

  # return max diference number if there are no distance found
  if not face_distances:
    return 1

  # Find a face with the greatest confidence and return then
  return max(face_distances)

if __name__ == '__main__':
  # Check if there are enough arguments
  if len(sys.argv) != 3:
    raise ValueError('The number of arguments is different from what was expected!')

  # Checks if all arguments are valid
  for i, arg in enumerate(sys.argv):
    # Skipt first argument check
    if i == 0:
      continue
    if not os.path.exists(arg):
      raise FileNotFoundError(f'path {arg} on arguments are not valid!')
    if not os.path.isfile(arg):
      raise FileNotFoundError(f'path {arg} is not a file path!')
    if not (arg.endswith('.jpg') or arg.endswith('.jpeg')):
      raise ValueError(f'File {arg} is not supported!')

  # Compare two files in arguments
  accuracy = compare_image_faces(sys.argv[1], sys.argv[2])
  is_match_check = 200 if accuracy < TOLERANCE else 400 # pylint: disable=invalid-name

  # Output the result as json string
  print(
    json.dumps(
      Result(
        difference = accuracy,
        is_match = is_match_check
      )
    )
  )
