// https://www.hackerrank.com/challenges/time-conversion/problem

use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'timeConversion' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

fn timeConversion(s: &str) -> String {
    let period: String = s.chars().rev().take(2).collect::<Vec<_>>().into_iter().rev().collect();
    
    let len = s.chars().count();
    let trimmed_str: String = s.chars().take(len - 2).collect();
    let time_parts: Vec<&str> = trimmed_str.split(':').collect();
    
    let mut hour: i32 = time_parts[0].parse().unwrap();
    
    if period == "PM" && hour != 12 {
        hour += 12;
    } else if period == "AM" && hour == 12 {
        hour = 0;
    }    
    let hour_str = format!("{:02}", hour);
    
    format!("{}:{}:{}", hour_str, time_parts[1], time_parts[2])
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let s = stdin_iterator.next().unwrap().unwrap();

    let result = timeConversion(&s);

    writeln!(&mut fptr, "{}", result).ok();
}

