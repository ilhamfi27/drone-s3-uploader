FROM python:3.8.10 as builder
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN pyinstaller --onefile main.py

FROM ubuntu:jammy-20231128 as final
COPY --from=builder /app/dist/main /usr/bin/app
ENTRYPOINT [ "/usr/bin/app" ]
