package model;

import java.util.Arrays;

public class SingleArray<T> implements IArray<T> {

    private Object[] array;

    public SingleArray () {
        array = new Object[0];
    }

    @Override
    public int size() {
        return array.length;
    }

    @Override
    public void add(T item) {
        resize();
        array[size() - 1] = item;
    }

    @Override
    @SuppressWarnings("unchecked")
    public T get(int index) {
        return (T)array[index];
    }

    private void resize() {
        Object[] newArray = new Object[size() + 1];
        System.arraycopy(array, 0, newArray, 0, size());
        array = newArray;
    }

    @Override
    public void add(T item, int index){ 
        resize();
        shift(index);
        array[index]=item;
    }

    // сдвигает с элемента pos на shift элементов 
    //'элементы не влезающие в массив удаляются'
    private void shift(int pos) {
        if (pos>=array.length) return;

        for (int i = array.length-1; i >=pos; i--){
            if (i-1<0){
                return;
            }           
            array[i]=array[i-1];
        }
            
    }

    @Override
    public T remove(int index){         
        Object[] newArray = new Object[size() - 1];
        int shift=0;
        T obj=null;
        for (int i = 0; i <array.length; i++){
            if(i==index){
                obj=(T)array[i];
                continue;
            }
            newArray[shift]=array[i];
            shift=shift+1;
        }
        array=newArray;
        return obj;
    }
}
