// Aqui que você faz todo seu código
use pyo3::prelude::*;

#[pyfunction]
fn add(a: i64, b: i64) -> i64 {
    a + b
}

#[pyfunction]
fn greet(name: &str) -> String {
    format!("Hello, {}! Welcome to Rust in Python!", name)
}

#[pyfunction]
fn comemora() {
    println!("COMEMORA FUNCIONOU!")
}

#[pyfunction]
fn fibonacci(n: u32) -> u64 {
    match n {
        0 => 0,
        1 => 1,
        _ => {
            let mut a = 0;
            let mut b = 0;
            for _ in 2..=n {
                let temp = a +b;
                a = b;
                b = temp
            }
            b
        }
    }
}

#[pymodule]
// o nome do modulo aqui deve ser igual ao do projeto iniciado em cargo init 
fn rusty_snek(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(add, m)?)?;
    m.add_function(wrap_pyfunction!(greet, m)?)?;
    m.add_function(wrap_pyfunction!(fibonacci, m)?)?;
    m.add_function(wrap_pyfunction!(comemora, m)?)?;
    Ok(())
}