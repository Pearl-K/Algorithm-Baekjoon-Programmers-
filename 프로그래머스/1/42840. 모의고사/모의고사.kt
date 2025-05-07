class Solution {
    fun solution(answers: IntArray): IntArray {
        var ans = intArrayOf()
        val one = intArrayOf(1, 2, 3, 4, 5)
        val two = intArrayOf(2, 1, 2, 3, 2, 4, 2, 5)
        val three = intArrayOf(3, 3, 1, 1, 2, 2, 4, 4, 5, 5)
        val scrs = intArrayOf(0, 0, 0)
        
        for(i in answers.indices) {
            if (answers[i] == one[i%one.size]) scrs[0]++
            if (answers[i] == two[i%two.size]) scrs[1]++
            if (answers[i] == three[i%three.size]) scrs[2]++
        }
        
        val maxScr = scrs.maxOrNull() ?: 0
        
        return scrs.withIndex()
            .filter { it.value == maxScr }
            .map { it.index + 1 }
            .toIntArray()
    }
}