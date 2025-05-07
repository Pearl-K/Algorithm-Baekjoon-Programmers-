import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine()!!.toInt()
    val k = br.readLine()!!.toInt()
    val st = StringTokenizer(br.readLine()!!)
    val arr = IntArray(n) { st.nextToken().toInt() }
    arr.sort()
    
    if (k >= n) {
        println(0)
        return
    }
    
    val diff = IntArray(n-1) {
        i -> arr[i+1]-arr[i]
    }
    diff.sort()
    
    var ret = 0
    for (i in 0 until n-k) {
        ret += diff[i]
    }
    println(ret)
}