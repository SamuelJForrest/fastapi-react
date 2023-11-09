import os
from dotenv import load_dotenv
import uvicorn

load_dotenv()

TEST = os.environ.get('TEST')
print(TEST)

if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)
