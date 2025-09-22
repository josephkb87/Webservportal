use axum::{routing::get, Router};
use std::net::SocketAddr;
use axum_server::Server;

async fn hello() -> &'static str {
    "Hello from Rust Backend 🚀"
}

#[tokio::main]
async fn main() {
    let app = Router::new().route("/hello", get(hello));
    let addr = SocketAddr::from(([127, 0, 0, 1], 8001));
    
    println!("Rust backend running at http://{}", addr);
    Server::bind(addr)
        .serve(app.into_make_service())
        .await
        .unwrap();
}

async fn start_server(addr: SocketAddr) {
    let server = Server::bind(addr).serve(Router);
    let app = Router::new().route("/", get(|| async { "Hello, world!" }));

    axum_server::bind(addr)
        .serve(app.into_make_service())
        .await
        .unwrap();
}