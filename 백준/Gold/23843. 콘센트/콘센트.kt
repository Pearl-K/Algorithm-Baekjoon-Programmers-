import java.io.*
import java.util.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (N, M) = br.readLine().split(" ").map { it.toInt() }
    val arr = br.readLine().split(" ").map { it.toInt() }
    val pq = PriorityQueue<Int>(compareByDescending { it })
    arr.forEach { pq.add(it) }
    val lastTime = IntArray(M)
    
    while(pq.isNotEmpty()) {
        val time = pq.poll()
        val idx = lastTime.withIndex().minByOrNull { it.value }!!.index
        lastTime[idx] += time
    }
    val ret = lastTime.maxOrNull()
    println(ret)
}