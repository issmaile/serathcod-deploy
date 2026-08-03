FROM node:20-slim

ENV NODE_ENV=production
ENV DATABASE_PATH=/app/data/serath.db
ENV PORT=4000

RUN mkdir -p /app/data /app/data/uploads

WORKDIR /app
COPY package.json ./

# better-sqlite3 is a native module — install build tools, compile it,
# then purge build tools in one layer to keep the image small.
RUN apt-get update \
  && apt-get install -y --no-install-recommends python3 make g++ \
  && npm install --omit=dev \
  && apt-get purge -y python3 make g++ \
  && apt-get autoremove -y --purge \
  && rm -rf /var/lib/apt/lists/*

COPY bundle.cjs ./
COPY frontend/dist ./frontend/dist/
COPY reset.cjs entrypoint.sh ./

VOLUME ["/app/data"]
EXPOSE 4000

CMD ["sh", "/app/entrypoint.sh"]
