use std::io;
use std::collections::HashMap;

fn multiples(n: usize) -> Vec<usize> {
    let mut res = Vec::new();
    for i in 1..f64::sqrt(n as f64) as usize + 1 {
        let d = n / i;
        let m = n % i;

        if m != 0 {
            continue
        } else if d == i {
            res.push(i);
        } else {
            res.push(i);
            res.push(d);
        }
    }
    res
}

fn test(n: usize) {
    for m in multiples(n) {
        println!("{}", m);
    }
    println!("");
}

fn main() -> io::Result<()> {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer)?;

    let n = buffer.replace('\n', "").parse::<usize>().unwrap();

    // part 1
    let mut i = 0;
    while multiples(i).iter().map(|x| x * 10).sum::<usize>() < n {
        i += 1;
    }
    println!("part 1 {}", i);

    i = 0;
    let mut hm: HashMap<usize, usize> = HashMap::new();
    while multiples(i).iter().map(|x| {
        let entry = hm.entry(*x).or_insert(0);
        if *entry > 50 {
            0
        } else {
            *entry += 1;
            x * 11
        }
    }).sum::<usize>() < n {
        i += 1;
    }
    println!("part 2 {}", i);

    Ok(())
}
