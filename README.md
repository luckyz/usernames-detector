# usernames-detector

Recognizes a username text from an screenshot of any social network, implementing Google Cloud Vision API

# Usage

Firstly, you must create a [Google Cloud Platform](https://cloud.google.com/docs/overview#projects) project (GCP) (see https://cloud.google.com/docs/overview#projects). Install [GCP SDK](https://cloud.google.com/sdk/docs/install) (https://cloud.google.com/sdk/docs/install), and [initialize](https://cloud.google.com/sdk/docs/initializing) it (https://cloud.google.com/sdk/docs/initializing).
Then, configure your GCP JSON file credentials in your project, setting the path in `GOOGLE_APPLICATION_CREDENTIALS` environment variable.
Finally, import `usernames-detector`, passing the screenshot path as parameter.

```python
import usernames-detector
print(text_text('your_screenshot_path')
```
