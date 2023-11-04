use std::io::{BufRead, self};

fn index(r: usize, c: usize) -> usize {
    let fst = (r * (r + 1)) / 2;
    let snd = ((r + c + 1) * (r + c + 2)) / 2;
    let thd = ((r + 1) * (r + 2)) / 2;
    return (fst + snd) - thd;
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines()
        .map(|res_s| res_s.unwrap());
    let line = lines.next().unwrap();
    let handler = line.split(" ");
    let mut map = handler.map(|s| s.parse::<usize>().unwrap());

    let r = map.next().unwrap();
    let c = map.next().unwrap();
    let mut res: isize = 20151125;
    let mult: isize =  252533;
    let md: isize = 33554393;

    for _ in 0..(index(r, c)) {
        res = (res * mult) % md;
    }

    println!("{}", res);

    Ok(())
}
