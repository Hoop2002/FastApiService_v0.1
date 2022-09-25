import uvicorn
from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse

import connectDataBase

app = FastAPI()


@app.get("/")
def root():
    return FileResponse("public/index.html")


@app.post("/postdata")
def postData(item=Form()):
    request_data_base = connectDataBase.requestDataBase(item)
    html_content = ""

    for i in request_data_base:
        html_content += f"<h4>{i}</h4>"

    if not request_data_base:
        return HTMLResponse(f"<h3>{item}</h3> <h4>Не найден</h4>")

    return HTMLResponse(f"<h2>Domain: {item}</h2>"
                        f"<h2>Ip: </h2>"
                        f"</h3> {html_content}</h3>")


if __name__ == "__main__":
    uvicorn.run(port=8080, host="127.0.0.1", app=app)
