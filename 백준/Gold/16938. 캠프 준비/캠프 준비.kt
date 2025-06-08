import java.io.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (N, L, R, X) = br.readLine()!!.split(" ").map { it.toInt() }
    val arr = br.readLine()!!.split(" ").map { it.toInt() }.toIntArray()
    var ans = 0

    for (i in 1 until (1 shl N)) {
        val comb = mutableListOf<Int>()

        for (j in 0 until N) {
            if ((i and (1 shl j)) != 0) {
                comb.add(arr[j])
            }
        }

        if (comb.size < 2) continue
        val combSum = comb.sum()
        val combDiff = comb.maxOrNull()!! - comb.minOrNull()!!
        if (combSum in L..R && combDiff >= X) ans++
    }
    println(ans)
}