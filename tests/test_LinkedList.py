"""The file contains unit tests for linked list class"""

from LinkedList import LinkedList


class TestLinkedLists:

    def test_append_empty(self) -> None:
        """test if append works on empty list"""
        lst = LinkedList()
        lst.append(0)

        assert lst.to_list() == [0]

    def test_append_with_elements(self) -> None:
        """test if the append works on list with elements"""
        lst = LinkedList([1, 2, 3])
        lst.append(0)

        assert lst.to_list() == [1, 2, 3, 0]

    def test_contains_true(self) -> None:
        """test __contains___ function for an element in the list"""
        lst = LinkedList([1, 2, 3])
        actual = (1 in lst)
        expected = True

        assert actual == expected

    def test_contains_false(self) -> None:
        """test __contains___ function for an element not in the list"""
        lst = LinkedList([1, 2, 3])
        actual = (4 in lst)
        expected = False

        assert actual == expected

    def test_getitem_index_bound(self) -> None:
        """test __getitem__ function for an index in the lst"""
        lst = LinkedList([1, 2, 3])
        actual = lst.__getitem__(1)
        expected = 2

        assert actual == expected

    def test_getitem_index_outbound(self) -> None:
        """test __getitem__ function for an index not in the lst"""
        lst = LinkedList([1, 2, 3])

        try:
            actual = lst.__getitem__(4)

        except IndexError:
            assert True

        except Exception as exp:
            if exp != IndexError:
                assert False

    def test_getitem_slice_inbounds(self) -> None:
        """Test __getitem__ for a slice with well defined bounds"""
        lst = LinkedList([0, 1, 2, 3, 4, 5, 6])

        assert lst[1: 5].to_list() == [1, 2, 3, 4]

    def test_getitem_slice_leftbound(self) -> None:
        """Test __getitem__ for a slice with well defined left bound but no right bound"""
        lst = LinkedList([0, 1, 2, 3, 4, 5, 6])

        assert lst[1:].to_list() == [1, 2, 3, 4, 5, 6]

    def test_getitem_slice_rightbound(self) -> None:
        """Test __getitem__ for a slice with well defined right bound but no left bound"""
        lst = LinkedList([0, 1, 2, 3, 4, 5, 6])

        assert lst[:4].to_list() == [0, 1, 2, 3]

    def test_pop_index_present(self) -> None:
        """test pop function when index in inbound"""
        lst = LinkedList([0, 1, 2, 3, 4, 5, 6])

        element = lst.pop(1)

        assert element == 1 and lst.to_list() == [0, 2, 3, 4, 5, 6]

    def test_pop_index_not_present(self) -> None:
        """test pop when index is out of bound"""
        lst = LinkedList([0, 1, 2, 3, 4, 5, 6])

        lst = LinkedList([1, 2, 3])

        try:
            actual = lst.pop(10)

        except IndexError:
            assert True

        except Exception as exp:
            if exp != IndexError:
                assert False

    def test_remove_element_present(self) -> None:
        """test remove function when element is present"""
        lst = LinkedList([0, 1, 2, 3, 4, 5, 6])

        lst.remove(2)

        assert lst.to_list() == [0, 1, 3, 4, 5, 6]

    def test_remove_element_absent(self) -> None:
        """test remove function when element is absent"""
        lst = LinkedList([0, 1, 2, 3, 4, 5, 6])

        try:
            lst.remove(10)

        except ValueError:
            assert True

        except Exception as exp:
            if exp != IndexError:
                assert False

    def test_index_element_present(self) -> None:
        """test index function when element is present"""
        lst = LinkedList([0, 1, 2, 3, 4, 5, 6])

        assert lst.index(2) == 2

    def test_index_element_absent(self) -> None:
        """test index function when element is absent"""
        lst = LinkedList([0, 1, 2, 3, 4, 5, 6])

        try:
            lst.index(10)

        except ValueError:
            assert True

        except Exception as exp:
            if exp != IndexError:
                assert False

    def test_count_element_present(self) -> None:
        """test count function when element is present"""
        lst = LinkedList([0, 1, 2, 2, 4, 5, 6])

        assert lst.count(2) == 2

    def test_count_element_absent(self) -> None:
        """test count function when element is absent"""
        lst = LinkedList([0, 1, 2, 3, 4, 5, 6])

        assert lst.count(10) == 0

    def test_setitem_index_present(self) -> None:
        """test __setitem__ function when index in inbound"""
        lst = LinkedList([0, 1, 2, 3, 4, 5, 6])

        lst.__setitem__(1, 100)

        assert lst.to_list() == [0, 100, 2, 3, 4, 5, 6]

    def test_setitem_index_not_present(self) -> None:
        """test __setitem__ when index is out of bound"""
        lst = LinkedList([0, 1, 2, 3, 4, 5, 6])

        try:
            lst.__setitem__(10, 100)
        except IndexError:
            assert True
        except Exception as exp:
            if exp != IndexError:
                assert False

    def test_extend_empty_empty(self) -> None:
        """test extend function on two empty lists"""
        lst1 = LinkedList()
        lst2 = LinkedList()

        lst1.extend(lst2)

        assert lst1.to_list() == []

    def test_extend_non_empty_empty(self) -> None:
        """test extend function on one non empty and one empty list"""
        lst1 = LinkedList([1, 2, 3, 4])
        lst2 = LinkedList()

        lst1.extend(lst2)

        assert lst1.to_list() == [1, 2, 3, 4]

    def test_extend_empty_non_empty(self) -> None:
        """test extend function on one non empty and one empty list"""
        lst1 = LinkedList([])
        lst2 = LinkedList([1, 2, 3, 4])

        lst1.extend(lst2)

        assert lst1.to_list() == [1, 2, 3, 4]

    def test_extend_non_empty_non_empty(self) -> None:
        """test extend function on both non empty list"""
        lst1 = LinkedList([1, 2, 3, 4])
        lst2 = LinkedList([5, 6, 7, 8])

        lst1.extend(lst2)

        assert lst1.to_list() == [1, 2, 3, 4, 5, 6, 7, 8]

    def test_add_empty_empty(self) -> None:
        """test __add__ function on two empty lists"""
        lst1 = LinkedList()
        lst2 = LinkedList()

        lst3 = lst1 + lst2

        assert lst3.to_list() == []

    def test_add_non_empty_empty(self) -> None:
        """test __add__ function on one non empty and one empty list"""
        lst1 = LinkedList([1, 2, 3, 4])
        lst2 = LinkedList()

        lst3 = lst1 + lst2

        assert lst3.to_list() == [1, 2, 3, 4]

    def test_add_non_empty_non_empty(self) -> None:
        """test __add__ function on both non empty list"""
        lst1 = LinkedList([1, 2, 3, 4])
        lst2 = LinkedList([5, 6, 7, 8])

        lst3 = lst1 + lst2

        assert lst3.to_list() == [1, 2, 3, 4, 5, 6, 7, 8]

