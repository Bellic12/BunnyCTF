# Multi-stage build: build static assets with pnpm (Vite), serve with Nginx.

# --- Build stage ---
FROM node:25-alpine AS build
WORKDIR /app

# Enable pnpm via Corepack (bundled with Node 25).
# Pin to a recent pnpm to keep builds reproducible.
RUN corepack enable && corepack prepare pnpm@latest --activate

# Copy only manifest files first for better layer caching.
# Keep pnpm-lock.yaml in the context so installs are deterministic.
COPY package.json ./
COPY pnpm-lock.yaml ./

# Install dependencies (frozen to lockfile).
RUN pnpm install --frozen-lockfile

# Copy the rest of the sources and build.
COPY . .
# Produces static files in /app/dist by default for Vite
RUN pnpm run build

# --- Runtime stage ---
FROM nginx:alpine
# Copy build output to Nginx web root.
COPY --from=build /app/dist /usr/share/nginx/html

# Expose HTTP
EXPOSE 80