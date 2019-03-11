import java.lang.*;
import java.util.Iterator;
import java.util.NoSuchElementException;

class IF {
    private int iter_index = 0;
    private Iterator<T>[] iterlist;
    public IF(Iterator<T>[] iterlist) {
        this.iterlist = iterlist;
    }
    public T next() throws NoSuchElementException {
        for(int i = 0; i < this.iterlist.length; i++) {
            int new_iter_index = this.iter_index + i % this.iterlist.length;
            if(iterlist[new_iter_index].hasNext()) {
                T val = iterlist[new_iter_index].next();
                iter_index = new_iter_index + 1 % this.iterlist.length;
                return val;
            }
        }
        throw NoSuchElementException;
    }

    public boolean hasNext() {
        for(int i = 0; i < this.iterlist.length; i++) {
            if(iterlist[i].hasNext()) {
                return true;
            }
        }
        return false;
    }
}


class array {
   public static void main(String[] args) {
        int[] arr1 = {1, 2, 3};
        int[] arr2 = {4, 5};
        int[] arr3 = {6, 7, 8, 9};
        Iterator<Integer> a = arr1.iterator();
        Iterator<Integer> b = arr2.iterator();
        Iterator<Integer> c = arr3.iterator();
        Iterator<Integer>[] iterlist = {a, b, c};
        IF itfl = new IF(iterlist);
        while(IF.hasNext()) {
            system.out.println(IF.next());
        }
    }
}
