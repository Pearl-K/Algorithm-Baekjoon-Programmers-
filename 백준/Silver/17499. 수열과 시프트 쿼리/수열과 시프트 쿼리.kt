import java.io.*
import java.util.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (N, Q) = br.readLine()!!.split(" ").map { it.toInt() }
    val arr = br.readLine()!!.split(" ").map { it.toInt() }.toIntArray()
    var start = 0
    
    repeat(Q) {
        val comms = br.readLine()!!.split(" ").map { it.toInt() }
        when (comms[0]) {
            1 -> {
                val i = comms[1]
                val x = comms[2]
                val idx = (start+i-1)%N
                arr[idx] += x
            }
            2 -> {
                val left = comms[1]
                start = (start-left+N)%N
            }
            3 -> {
                val right = comms[1]
                start = (start+right)%N
            }
        }
    }
    val ret = IntArray(N) { arr[(start+it)%N] }
    println(ret.joinToString(" "))
}