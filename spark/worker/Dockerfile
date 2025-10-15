FROM bde2020/spark-base:3.3.0-hadoop3.3

LABEL maintainer="Gezim Sejdiu <g.sejdiu@gmail.com>, Giannis Mouchakis <gmouchakis@gmail.com>"

# --- Sanofi Root + Technical CA (système + Java) ---
COPY sanofi-bundle.crt /usr/local/share/ca-certificates/sanofi-bundle.crt
RUN set -eux; \
    apt-get update -qq; \
    apt-get install -y -qq ca-certificates wget; \
    update-ca-certificates; \
    CACERTS="$(dirname "$(readlink -f "$(which java)")")/../lib/security/cacerts"; \
    keytool -importcert -trustcacerts -noprompt \
      -alias sanofi-bundle \
      -file /usr/local/share/ca-certificates/sanofi-bundle.crt \
      -keystore "$CACERTS" -storepass changeit; \
    keytool -list -keystore "$CACERTS" -storepass changeit | grep -i sanofi || true
# --- End Sanofi Root + Technical CA ---

COPY worker.sh /worker.sh

ENV SPARK_WORKER_WEBUI_PORT=8081 \
    SPARK_WORKER_LOG=/spark/logs \
    SPARK_MASTER=spark://spark-master:7077

EXPOSE 8081
CMD ["/bin/bash", "/worker.sh"]
