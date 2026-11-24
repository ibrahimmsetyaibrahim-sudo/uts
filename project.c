#include <stdio.h>
#include <math.h>
#include <ctype.h>

int main() {
    char nama_hp[100];
    float harga, ongkir, target, nominal;
    int pilihan, hari = 0, minggu = 0, bulan = 0;

    printf("========================================\n");
    printf("             HITUNG HAPEKU              \n");
    printf("========================================\n");

    printf(" MASUKKAN NAMA HP       : ");
    scanf(" %[^\n]", nama_hp);
    printf("HARGA HP (Rp)           : ");
    scanf("%f", &harga);
    printf("BIAYA PENGIRIMAN (Rp)   : ");
    scanf("%f", &ongkir);

    target = harga + ongkir;

    printf("\n--- CARA NABUNG ---\n1. Per Hari\n2. Per Minggu\n3. Per Bulan\nPilihan (1/2/3): ");
    scanf("%d", &pilihan);

    if (pilihan < 1 || pilihan > 3) {
        printf("\n[Peringatan] Pilihan tidak valid!\n");
        return 0;
    }

    printf("Masukkan nominal (Rp): ");
    scanf("%f", &nominal);

    if (nominal <= 0) {
        printf("\n[Error] Nominal harus lebih dari 0!\n");
        return 0;
    }

    // Hitung waktu berdasarkan pilihan
    int durasi = (int)ceil(target / nominal);
    float sisa = (durasi * nominal) - target;

    if (pilihan == 1) {
        hari = durasi;
        minggu = hari / 7;
        bulan = hari / 30;
    } else if (pilihan == 2) {
        minggu = durasi;
        hari = minggu * 7;
        bulan = minggu / 4;
    } else {
        bulan = durasi;
        hari = bulan * 30;
    }

    // Output Hasil
    printf("\n      HASIL TARGET CELENGAN: %s\n", nama_hp);
    printf("Total Target Biaya    : Rp %.0f\n", target);
    printf("Waktu yang Dibutuhkan : %d %s\n", durasi, pilihan==1?"hari":pilihan==2?"minggu":"bulan");
    printf("Estimasi Lain         : ± %d hari / %d minggu / %d bulan\n", hari, minggu, bulan);
    printf("Sisa/Kelebihan Uang   : Rp %.0f\n", sisa);
    printf("\n Semangat terus menabung demi HP impian\n");

    return 0;
}