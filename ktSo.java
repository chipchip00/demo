package javaapplication1;

public class ktSo {

    private int so;

    ktSo(int so) {
        this.so = so;
    }

    public boolean soNguyenTo() {
        int dem = 0;
        for (int i = 2; i < so; i++) {
            if (so % i == 0) {
                dem++;
            }
        }
        if (dem == 0 && so != 1) {
            return true;
        } else {
            return false;
        }
    }

    public boolean soChinhPhuong() {
        int dem1 = 0;
        for (int i = 1; i < so; i++) {
            if (i * i == so) {
                dem1++;
            }
        }
        if (dem1 == 1) {
            return true;
        } else {
            return false;
        }
    }

    public boolean soHoanHao() {
        int s = 0;
        for (int i = 1; i < so; i++) {
            if (so % i == 0) {
                s += i;
            }
        }
        if (s == so) {
            return true;
        } else {
            return false;
        }
    }
}
