"""The file contains tests for Queue class"""

from Queue import *

# Add the root directory to PYTHONPATH
import sys
sys.path.append('.')


class TestQueue:

    def test_enqueue_empty(self) -> None:
        """Test enqueue function on empty queue"""
        queue = Queue()
        queue.enqueue(0)

        actual = queue.to_list()
        expected = [0]

        assert actual == expected

    def test_enqueue_filled(self) -> None:
        """Test enqueue function on filled queue"""
        queue = Queue([1, 2, 3])
        queue.enqueue(0)

        actual = queue.to_list()
        expected = [0, 1, 2, 3]

        assert actual == expected

    def test_enqueue_filled_to_limit(self) -> None:
        """Test enqueue function on queue filled to limit"""
        queue = Queue([1, 2, 3], limit=3)

        try:
            queue.enqueue(0)
        except QueueLimitReachedError:
            assert True
        except Exception as exp:
            if exp != QueueLimitReachedError:
                assert False

    def test_enqueue_multiple(self) -> None:
        """Test enqueue multiple times"""
        queue = Queue([6, 7, 8])

        queue.enqueue(5)
        queue.enqueue(4)
        queue.enqueue(3)
        queue.enqueue(2)

        actual = queue.to_list()
        expected = [2, 3, 4, 5, 6, 7, 8]

        assert actual == expected

    def test_dequeue_empty(self) -> None:
        """Test dequeue on an empty queue"""
        queue = Queue()

        try:
            queue.dequeue()
        except EmptyQueueError:
            assert True
        except Exception as exp:
            if exp != EmptyQueueError:
                assert False

    def test_dequeue_filled(self) -> None:
        """Test dequeue for a filled stack"""
        queue = Queue([1, 2, 3, 4, 5])

        queue.dequeue()
        queue.dequeue()
        queue.dequeue()

        actual = queue.to_list()
        expected = [1, 2]

        assert actual == expected

    def test_extend_no_limit(self) -> None:
        """Test extend function when there is no limit"""
        q1 = Queue([5, 6, 7])
        q2 = Queue([1, 2, 3, 4])

        q1.extend(q2)

        actual = q1.to_list()
        expected = [1, 2, 3, 4, 5, 6, 7]

        assert actual == expected

    def test_extend_limit(self) -> None:
        """Test extend function when there is a limit"""
        q1 = Queue([5, 6, 7], limit=4)
        q2 = Queue([1, 2, 3, 4])

        q1.extend(q2)

        actual = q1.to_list()
        expected = [4, 5, 6, 7]

        assert actual == expected

    def test_map(self) -> None:
        """Test map function"""
        queue = Queue([1, 2, 3])
        queue.map(lambda x: x ** 2)

        actual = queue.to_list()
        expected = [1, 4, 9]

        assert actual == expected
