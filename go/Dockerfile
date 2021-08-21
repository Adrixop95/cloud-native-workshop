FROM golang:1.17-alpine

WORKDIR /app 

COPY go.mod go.sum main.go /app/

RUN go build -o main .

CMD "/app/main"