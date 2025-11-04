import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val st = StringTokenizer(readLine())
    val n = st.nextToken().toInt()
    val x = st.nextToken().toInt()
    
    val visitors = readLine().split(" ").map { it.toInt() }
    var sum = visitors.take(x).sum()
    var maxSum = sum
    var count = 1

    for (i in x until n) {
        sum += visitors[i] - visitors[i-x]

        when {
            sum > maxSum -> {
                maxSum = sum
                count = 1
            }
            sum == maxSum -> count++
        }
    }

    if (maxSum == 0) println("SAD")
    else {
        println(maxSum)
        println(count)
    }
}