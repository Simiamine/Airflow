FROM bde2020/spark-base:3.3.0-hadoop3.3

LABEL maintainer="Gezim Sejdiu <g.sejdiu@gmail.com>, Giannis Mouchakis <gmouchakis@gmail.com>"

# --- Sanofi Root + Technical CA (système + Java) ---
COPY sanofi-bundle.crt /usr/local/share/ca-certificates/sanofi-bundle.crt
RUN set -eux; \
    apt-get update -qq; \
    apt-get install -y -qq ca-certificates wget; \
    update-ca-certificates; \
    # Import dans le keystore Java (Spark/Hadoop)
    CACERTS="$(dirname "$(readlink -f "$(which java)")")/../lib/security/cacerts"; \
    keytool -importcert -trustcacerts -noprompt \
      -alias sanofi-bundle \
      -file /usr/local/share/ca-certificates/sanofi-bundle.crt \
      -keystore "$CACERTS" -storepass changeit; \
    keytool -list -keystore "$CACERTS" -storepass changeit | grep -i sanofi || true
# --- End Sanofi Root + Technical CA ---

COPY master.sh /

RUN wget -q https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.2/hadoop-aws-3.3.2.jar \
 && wget -q https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.11.1026/aws-java-sdk-bundle-1.11.1026.jar \
 && mv hadoop-aws-3.3.2.jar /spark/jars/ \
 && mv aws-java-sdk-bundle-1.11.1026.jar /spark/jars/

ENV SPARK_MASTER_PORT=7077 \
    SPARK_MASTER_WEBUI_PORT=8080 \
    SPARK_MASTER_LOG=/spark/logs

EXPOSE 8080 7077 6066
CMD ["/bin/bash", "/master.sh"]
