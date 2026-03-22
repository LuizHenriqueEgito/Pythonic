use rayon::prelude::*;
use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
fn is_prime(n: u64) -> bool {
    if n < 2 {
        return false;
    }
    if n == 2 {
        return true;
    }
    if n % 2 == 0 {
        return false;
    }

    let limit = (n as f64).sqrt() as u64;

    let mut i = 3;
    while i <= limit {
        if n % i == 0 {
            return false;
        }
        i += 2;
    }

    true
}

#[pyfunction]
fn parallel_worker(numbers: Vec<u64>) -> Vec<u64> {
    numbers
        .par_iter()
        .cloned()
        .filter(|&n| is_prime(n))
        .collect()
}

#[pymodule]
fn prime_numbers_fn(m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(parallel_worker, m)?)?;
    m.add_function(wrap_pyfunction!(is_prime, m)?)?;
    Ok(())
}