FROM quay.io/astronomer/astro-runtime:12.9.0-base

COPY sanofi-bundle.pem /usr/local/share/ca-certificates/sanofi-bundle.crt

USER root
RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends ca-certificates curl; \
    update-ca-certificates; \
    rm -rf /var/lib/apt/lists/*

ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt \
    SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt \
    UV_NATIVE_TLS=true

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

USER astro
