from fastapi.middleware.cors import CORSMiddleware

origins = [
    "*"
]

def get_cors_middleware():
    return CORSMiddleware(allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
