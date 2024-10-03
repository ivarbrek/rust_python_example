use pyo3::prelude::*;
use std::collections::HashMap;


fn fibonacci(n: u64, memo: &mut HashMap<u64, u64>) -> u64 {
    if n == 0 {
        return 0;
    } else if n == 1 {
        return 1;
    }

    if let Some(&result) = memo.get(&n) {
        return result;
    }

    let result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo);
    memo.insert(n, result);
    result
}

#[pyfunction]
fn compute_fibonacci(n: u64) -> u64 {
    let mut memo = HashMap::new();
    fibonacci(n, &mut memo)
}


#[pyfunction]
fn get_all_numbers(n: u64) -> Vec<u64> {
    (0..n).into_iter().collect()
}

/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn example_module(_py: Python, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(compute_fibonacci, m)?)?;
    m.add_function(wrap_pyfunction!(get_all_numbers, m)?)?;
    Ok(())
}
