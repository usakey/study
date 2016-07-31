package recfun

import scala.annotation.tailrec

object Main {
  def main(args: Array[String]) {
    println("Pascal's Triangle")
    for (row <- 0 to 10) {
      for (col <- 0 to row)
        print(pascal(col, row) + " ")
      println()
    }
  }

  /**
   * Exercise 1
   */
    def pascal(c: Int, r: Int): Int =
      if (c != 0 && r != 0 && c != r) pascal(c-1,r-1) + pascal(c, r-1)
      else 1

  
  /**
   * Exercise 2
   */
    def balance(chars: List[Char]): Boolean = {
      @tailrec
      def f(chars: List[Char], cnt: Int): Boolean =
        chars match{
          case Nil => cnt == 0
          case '(' :: x => f(x, cnt + 1)
          case ')' :: x => (cnt > 0) && f(x, cnt - 1)
          case _ => f(chars.tail, cnt)
        }
      f(chars, 0)
  }
  
  /**
   * Exercise 3
   */
    def countChange(money: Int, coins: List[Int]): Int = {
      money match {
        case 0 => 1
        case x if x < 0 => 0
        case x if x > 0 && coins.isEmpty => 0
        case _ => countChange(money, coins.tail) + countChange(money - coins.head, coins)
      }
  }
  }
