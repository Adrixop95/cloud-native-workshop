FROM golang:1.20-alpine as build

WORKDIR /app 

COPY go.mod go.sum main.go /app/

RUN go build -o cars .

FROM alpine:3.17 as publish
WORKDIR /app

COPY --from=build /app/cars /app/cars

ENTRYPOINT [ "/app/cars" ]