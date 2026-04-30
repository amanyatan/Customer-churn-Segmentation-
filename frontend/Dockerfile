# Stage 1: Build the React application
FROM node:20-alpine AS builder

WORKDIR /app

# Install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy source code and build
COPY . .
RUN npm run build

# Stage 2: Serve the app using Vite's preview or Nginx
# Here we use node to run a lightweight server or run vite preview
FROM node:20-alpine

WORKDIR /app

COPY --from=builder /app/dist ./dist
COPY package.json ./

# Install serve
RUN npm install -g serve

EXPOSE 5173

# Serve on 5173 to match the expected docker-compose port
CMD ["serve", "-s", "dist", "-l", "5173"]
