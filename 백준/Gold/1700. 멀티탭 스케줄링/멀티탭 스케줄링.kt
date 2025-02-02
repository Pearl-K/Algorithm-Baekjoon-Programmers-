import java.util.*

fun main() = with(System.`in`.bufferedReader()) {
    val (N, K) = readLine().split(' ').map { it.toInt() }
    val items = readLine().split(" ").map { it.toInt() }
    val plugSet = mutableSetOf<Int>()
    var ret = 0

    for (i in items.indices) {
        val item = items[i]
        if (item in plugSet) continue
        if (plugSet.size < N) {
            plugSet.add(item)
            continue
        }

        var lastItem = -1
        var targetToRemove = -1
        for (plug in plugSet) {
            val nextUse = items.subList(i+1, items.size).indexOf(plug)
            if (nextUse == -1) {
                targetToRemove = plug
                break
            }
            if (nextUse > lastItem) {
                lastItem = nextUse
                targetToRemove = plug
            }
        }
        plugSet.remove(targetToRemove)
        plugSet.add(item)
        ret++
    }
    println(ret)
}
