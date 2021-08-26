ARG IMAGE=
FROM ${IMAGE}

RUN apk --update add --no-cache ip6tables
