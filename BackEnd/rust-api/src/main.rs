// backend/rust-api/src/main.rs
use axum::{routing::get, Router};
use std::net::SocketAddr;

async fn hello() -> &'static str {
    "Hello from Rust Backend 🚀"
}

#[tokio::main]
async fn start_server(addr: SocketAddr) {
    let app = Router::new().route("/hello", get(|| async { "Hello, world!" }));
    let server = hyper::server::Server::bind(&addr).serve(router);
    let addr = SocketAddr::from(([127, 0, 0, 1], 8001));
    println!("Rust backend running at http://{}", addr);
    axum_Server::bind(addr)
        .serve(app.into_make_service())
        .await
        .unwrap();
}