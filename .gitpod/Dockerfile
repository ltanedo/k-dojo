# FROM gitpod/workspace-base:2024-08-20-00-26-31
# # # Copy project source code
# COPY . .

# FROM gitpod/workspace-rust:2024-07-14-17-19-51 
FROM gitpod/workspace-full:2024-08-08-14-54-59 

WORKDIR /workspace/k-dojo
RUN rustc --version
RUN cargo --version
RUN rustup --version
RUN python --version
RUN node --version
COPY . .

# FROM gitpod/workspace-python-3.12:2024-01-08-20-24-21
# COPY . .


# FROM gitpod/workspace-node-20:2024-08-12-04-59-05
# COPY . .



# # Build the project
# # RUN cargo build --release

# FROM alpine:latest
# RUN apk --no-cache add ca-certificates
# COPY --from=builder /home/rust/src/target/x86_64-unknown-linux-musl/release/rust-starter /usr/local/bin/rust-starter
# CMD ["/usr/local/bin/rust-starter"]
