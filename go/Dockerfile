FROM golang:1.17-alpine as build

WORKDIR /app 

COPY go.mod go.sum main.go /app/

RUN go build -o cars .

FROM alpine:3.14 as publish
WORKDIR /app

COPY --from=build /app/cars /app/cars

CMD "/app/cars"