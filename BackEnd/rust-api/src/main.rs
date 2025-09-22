use axum::{routing::get, Router};
use std::net::SocketAddr;

async fn hello() -> &'static str {
    "Hello from Rust Backend 🚀"
}

#[tokio::main]
async fn main() {
    let app = Router::new().route("/hello", get(hello));
    let addr = SocketAddr::from(([127, 0, 0, 1], 8001));
    println!("Rust backend running at http://{}", addr);
    axum::Server::bind(&addr)
        .serve(app.into_make_service())
        .await
        .unwrap();
}