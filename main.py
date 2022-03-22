import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="usernames-detector.json"


def detect_text(path, platform="instagram"):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    texts_list = []
    bounds = []

    for text in texts:
        texts_list.extend(text.description.split("\n"))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    if platform == "instagram":
        username_text = texts_list[::-1][0]
        username = username_text[:len(username_text) - 1]

    return username
    