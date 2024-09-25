from singly_linked_list import SinglyLinkedList

def test_append():
    linked_list = SinglyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    assert linked_list.head.data == 1
    assert linked_list.head.next.data == 2
    assert len(linked_list) == 2

def test_prepend():
    linked_list = SinglyLinkedList()
    linked_list.prepend(2)
    linked_list.prepend(1)
    assert linked_list.head.data == 1
    assert linked_list.head.next.data == 2
    assert len(linked_list) == 2

def test_insert():
    linked_list = SinglyLinkedList()
    linked_list.append(1)
    linked_list.append(3)
    linked_list.insert(1, 2)
    assert linked_list[0] == 1
    assert linked_list[1] == 2
    assert linked_list[2] == 3

def test_extend():
    linked_list = SinglyLinkedList()
    linked_list.extend([1, 2, 3])
    assert linked_list[0] == 1
    assert linked_list[1] == 2
    assert linked_list[2] == 3
    assert len(linked_list) == 3

def test_delete():
    linked_list = SinglyLinkedList()
    linked_list.extend([1, 2, 3])
    linked_list.delete(2)
    assert linked_list[0] == 1
    assert linked_list[1] == 3
    assert len(linked_list) == 2

def test_delete_at():
    linked_list = SinglyLinkedList()
    linked_list.extend([1, 2, 3])
    linked_list.delete_at(1)
    assert linked_list[0] == 1
    assert linked_list[1] == 3
    assert len(linked_list) == 2

def test_remove_duplicates():
    linked_list = SinglyLinkedList()
    linked_list.extend([1, 2, 2, 3])
    linked_list.remove_duplicates()
    assert linked_list[0] == 1
    assert linked_list[1] == 2
    assert linked_list[2] == 3
    assert len(linked_list) == 3

def test_clear():
    linked_list = SinglyLinkedList()
    linked_list.extend([1, 2, 3])
    linked_list.clear()
    assert len(linked_list) == 0
    assert linked_list.is_empty()

def test_find():
    linked_list = SinglyLinkedList()
    linked_list.extend([1, 2, 3])
    assert linked_list.find(2) == 1
    assert linked_list.find(4) is None

def test_reverse():
    linked_list = SinglyLinkedList()
    linked_list.extend([1, 2, 3])
    linked_list.reverse()
    assert linked_list[0] == 3
    assert linked_list[1] == 2
    assert linked_list[2] == 1

def test_is_empty():
    linked_list = SinglyLinkedList()
    assert linked_list.is_empty()
    linked_list.append(1)
    assert not linked_list.is_empty()

def test_get_set_item():
    linked_list = SinglyLinkedList()
    linked_list.extend([1, 2, 3])
    assert linked_list[1] == 2
    linked_list[1] = 4
    assert linked_list[1] == 4

def test_del_item():
    linked_list = SinglyLinkedList()
    linked_list.extend([1, 2, 3])
    del linked_list[1]
    assert linked_list[0] == 1
    assert linked_list[1] == 3

def test_len():
    linked_list = SinglyLinkedList()
    linked_list.extend([1, 2, 3])
    assert len(linked_list) == 3

def test_eq():
    list1 = SinglyLinkedList()
    list2 = SinglyLinkedList()
    list1.extend([1, 2, 3])
    list2.extend([1, 2, 3])
    assert list1 == list2

    list2.append(4)
    assert list1 != list2

def test_add():
    list1 = SinglyLinkedList()
    list2 = SinglyLinkedList()
    list1.extend([1, 2])
    list2.extend([3, 4])
    new_list = list1 + list2
    print(list1, list2)
    print(new_list)
    assert new_list[0] == 1
    assert new_list[1] == 2
    assert new_list[2] == 3
    assert new_list[3] == 4

def test_contains():
    linked_list = SinglyLinkedList()
    linked_list.extend([1, 2, 3])
    assert 2 in linked_list
    assert 4 not in linked_list

def test_iter():
    linked_list = SinglyLinkedList()
    linked_list.extend([1, 2, 3])
    assert list(iter(linked_list)) == [1, 2, 3]

def test_reversed():
    linked_list = SinglyLinkedList()
    linked_list.extend([1, 2, 3])
    assert list(reversed(linked_list)) == [3, 2, 1]

def test_str_repr():
    linked_list = SinglyLinkedList()
    linked_list.extend([1, 2, 3])
    assert str(linked_list) == '[1, 2, 3]'
    assert repr(linked_list) == '[1, 2, 3]'