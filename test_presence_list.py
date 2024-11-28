""" Test face recognition script """
from presence_list import compare_image_faces, TOLERANCE

def test_images_with_same_face(monkeypatch, capsys):
  """ Test script with images os same person """
  person1_image1 = './samples/person1_image1.jpg'
  person1_image2 = './samples/person1_image0.jpg'
  difference = compare_image_faces(person1_image1, person1_image2)
  assert difference < TOLERANCE
def test_images_with_different_faces(monkeypatch, capsys):
  """ Test script with images of different persons"""
  person1_image1 = './samples/person1_image0.jpg'
  person1_image2 = './samples/person2_image0.jpg'
  difference = compare_image_faces(person1_image1, person1_image2)
  assert difference > TOLERANCE