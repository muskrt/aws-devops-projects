FROM golang:1.22-alpine
WORKDIR /01
COPY go.mod ./
RUN go mod download
COPY *.go ./
RUN go build -o .
EXPOSE 8080
CMD [ "./01" ]