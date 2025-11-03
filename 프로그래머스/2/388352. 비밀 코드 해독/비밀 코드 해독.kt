class Solution {
    private var n: Int = 0
    private lateinit var q: Array<IntArray>
    private lateinit var ans: IntArray
    private var answer = 0
    
    private fun comb(start: Int, current: MutableList<Int>) {
        if (current.size == 5) {
            if (validate(current)) answer++
            return
        }
        for (i in start..n) {
            current.add(i)
            comb(i+1, current)
            current.removeAt(current.size-1)
        }
    }
    
    private fun validate(comb: List<Int>): Boolean {
        val set = comb.toHashSet()
        
        for (i in q.indices) {
            var cnt = 0
            for (num in q[i]) if (num in set) cnt++
            if (cnt != ans[i]) return false
        }
        return true
    }
    
    fun solution(n: Int, q: Array<IntArray>, ans: IntArray): Int {
        this.n = n
        this.q = q
        this.ans = ans
        answer = 0
        comb(1, mutableListOf())
        return answer
    }
}
