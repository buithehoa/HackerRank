package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
    "strconv"
    "strings"
)

/*
 * Complete the 'plusMinus' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

func plusMinus(arr []int32) {
    // Write your code here
    positiveCount := 0
    negativeCount := 0
    zeroCount := 0
    arrLength := float64(len(arr))
    
    for _, number := range arr {
        if number > 0 {
            positiveCount++
        } else if number < 0 {
            negativeCount ++
        } else {
            zeroCount++
        }
    }
    
    fmt.Println(fmt.Sprintf("%.6f", float64(positiveCount) / arrLength))
    fmt.Println(fmt.Sprintf("%.6f", float64(negativeCount) / arrLength))
    fmt.Println(fmt.Sprintf("%.6f", float64(zeroCount) / arrLength))
}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

    nTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
    checkError(err)
    n := int32(nTemp)

    arrTemp := strings.Split(strings.TrimSpace(readLine(reader)), " ")

    var arr []int32

    for i := 0; i < int(n); i++ {
        arrItemTemp, err := strconv.ParseInt(arrTemp[i], 10, 64)
        checkError(err)
        arrItem := int32(arrItemTemp)
        arr = append(arr, arrItem)
    }

    plusMinus(arr)
}

func readLine(reader *bufio.Reader) string {
    str, _, err := reader.ReadLine()
    if err == io.EOF {
        return ""
    }

    return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
    if err != nil {
        panic(err)
    }
}

