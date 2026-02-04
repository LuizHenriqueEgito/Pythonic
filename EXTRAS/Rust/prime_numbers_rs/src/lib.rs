use pyo3::prelude::*;

#[pyfunction]
fn is_prime_rust(n: usize) -> Vec<bool> {
    let mut result = Vec::with_capacity(n);

    for x in 0..n {
        if x < 2 {
            result.push(false);
            continue;
        }
        if x == 2 || x == 3 {
            result.push(true);
            continue;
        }
        if x % 2 == 0 || x % 3 == 0 {
            result.push(false);
            continue;
        }
        let limit = (x as f64).sqrt() as usize + 1;
        let mut is_prime = true;

        let mut i = 5;
        while i < limit {
            if x % i == 0 || x % (i + 2) == 0 {
                is_prime = false;
                break;
            }
            i += 6;
        }
        result.push(is_prime);
    }
    result
}

#[pymodule]
fn prime_numbers_rs(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(is_prime_rust, m)?)?;
    Ok(())
}
