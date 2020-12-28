import java.util.*;


class ByteSize {

    public static int getByteSize(String str)
    {
        byte[] byteArr = str.getBytes();

        return byteArr.length;
    }

    public static void main(String[] args) {
        getByteSize("19021522518328");
        System.out.println(getByteSize("19021522518328"));
    }
}