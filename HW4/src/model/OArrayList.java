package model;

public class OArrayList<T> implements IArray<T> {

    private java.util.ArrayList<T> array;

    public OArrayList() {
        array=new java.util.ArrayList<T>();
    }


    @Override
    public int size() {
        return array.size();
    }

    @Override
    public void add(T item) {
        array.add(item);
    }

    @Override
    @SuppressWarnings("unchecked")
    public T get(int index) {
        return array.get(index);
    }

    
    public void add(T item, int index){ 
        array.add(index, item);
    }

    

    @Override
    public T remove(int index){         
        return array.remove(index);
    }
}
