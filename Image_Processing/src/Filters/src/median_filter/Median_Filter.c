#include<stdio.h>
#include<string.h>
#include<math.h>
#include<time.h>
#define W_MAX 1
#define ROW 512
#define COL 512
#define T1 15
#define T2 25

double P[50]; double img[700][700]; double orig[512][512];

// Utility Function - Creates input image matrix
double getImg(char *s){
	FILE *fp;
	int i, j, r, c; double d, MSE = 0, dim = ROW * COL;
	fp = fopen(s, "r");
	// Create Matrix
	for(i = W_MAX; i < ROW+W_MAX; i++){
		for(j = W_MAX; j < COL+W_MAX; j++){
			fscanf(fp, "%lf ", &d);
			img[i][j] = d;
			MSE += pow((orig[i-W_MAX][j-W_MAX] - img[i][j]), 2);
			// Padding
			if (i == W_MAX){
				for(r = i-1; r >= i-W_MAX; r--) img[r][j] = img[i][j];
			}
			if(i == W_MAX + ROW - 1){
				for(r = i+1; r <= i+W_MAX; r++) img[r][j] = img[i][j];
			}
			if(j == W_MAX){
				for(c = j-1; c >= j-W_MAX; c--) img[i][c] = img[i][j];
			}
			if(j == W_MAX + COL - 1){
				for(c = j+1; c <= j+W_MAX; c++) img[i][c] = img[i][j];
			}
		}
	}
	// Corner Padding
	// Upper Corners
	for(i = 0; i < W_MAX; i++){
		// Left Corner
		for(j = 0; j < W_MAX; j++)
			img[i][j] = img[W_MAX][W_MAX];
		// Right Corner
		for(j = W_MAX+ COL; j< W_MAX+COL+W_MAX;j++)
			img[i][j] = img[W_MAX][W_MAX+COL-1];
	}
	// Lower Corners
	for(i = W_MAX+ROW; i < W_MAX+ROW+W_MAX; i++){
		// Left Corner
		for(j = 0; j < W_MAX; j++)
			img[i][j] = img[W_MAX+ROW-1][W_MAX];
		// Right Corner
		for(j = W_MAX+ COL; j< W_MAX+COL+W_MAX;j++)
			img[i][j] = img[W_MAX+ROW-1][W_MAX+COL-1];
	}

	fclose(fp);
	MSE /= dim;
	return MSE;
}

// Utility Function - Saves output image
double saveImg(char *s){
	FILE *fp;
	fp = fopen(s, "w");
	// Change According to size
	fprintf(fp, "P2 512 512 255\n");
	int i, j; double MSE = 0, dim = ROW*COL;
	for(i = W_MAX; i < ROW + W_MAX; i++){
		for(j = W_MAX; j< COL + W_MAX; j++){
			MSE += pow((orig[i-W_MAX][j-W_MAX] - img[i][j]), 2);
			fprintf(fp, "%d ", (int)img[i][j]);
		}
	}
	fclose(fp);
	MSE /= dim;
	return MSE;
}

// Calculates Structural Similarity Index of Images
double getSSIM(){
	double C1 = pow(0.01*255, 2), C2 = pow(0.03*255, 2), dim = ROW * COL;
	double Vx = 0, Vy = 0, COV = 0, SSIM, o, e;
	int i, j, ux = 0, uy = 0;
	for(i = W_MAX; i < ROW + W_MAX; i++){
		for(j = W_MAX; j< COL + W_MAX; j++){
			ux += orig[i-W_MAX][j-W_MAX];
			uy += img[i][j];			
		}
	}
	ux /= dim; uy /= dim;
	for(i = W_MAX; i < ROW + W_MAX; i++){
		for(j = W_MAX; j< COL + W_MAX; j++){
			o = orig[i-W_MAX][j-W_MAX];
			e = img[i][j];
			Vx += pow((o-ux),2);
			Vy += pow((e-uy), 2);
			COV += (o-ux)*(e-uy);
		}
	}
	Vx /= dim; Vy /= dim;
	COV /= dim;
	SSIM = ((2*ux*uy + C1) * (2*COV + C2))/((pow(ux, 2) + pow(uy, 2) + C1) * (Vx + Vy + C2));
	return SSIM;
}

// Utility - Returns median of first n numbers in P
double Median(int n){
	int i, d; double t, ans;
	// Sort the array - Insertion sort
	for(i = 1; i < n; i++){
		d = i;
		while (d > 0 && P[d] < P[d-1]){
			t = P[d];
			P[d] = P[d-1];
			P[d-1] = t;
			d--;
		}
	}
	// If n odd return mid element
	if (n&1)
		ans = P[n/2];
	// Else retuen
	else
		ans = (P[n/2 - 1] + P[n/2])/2;
	return ans;
}

// Filter - Median Filtering
double Filter(int r, int c){
	int cnt = 0, i, j, w=1; double M;
	for(i = r-w; i <= r+w; i++){
			for(j = c-w; j <= c+w; j++){
			P[cnt++] = img[i][j];
		}
	}
	M = Median(cnt);
	return M;
}

// Standard Median Filtering
double SMF(char *s){
	int i, j; double MSE;
	for(i = W_MAX; i < ROW + W_MAX; i++){
		for(j = W_MAX; j < COL + W_MAX; j++){
			// if(img[i][j]==0 || img[i][j]==255)
				img[i][j] = Filter(i, j);
		}
	}
	// Metric Calculation
	MSE = saveImg(s);
	return MSE;
}

int main() {
   int i, j; 
   clock_t start, end; double CPU_TIME;
   double MAXINT = pow(255, 2), RMSE, MSE1, MSE2, PSNR, d, IEF, SSIM;

   // Get Original Image for PSNR calculation
   FILE *fp;
   fp = fopen("Original_Image.pgm", "r");
   for(i = 0; i < ROW; i++){
	   	for(j = 0; j < COL; j++){
	   		fscanf(fp, "%lf ", &d);
	   		orig[i][j] = d;
	   	}
   }
   fclose(fp);

   start = clock();
   // Replace this with the src image name and the dest image name where the image needs to be saved
   MSE1 = getImg("Src Image");
   MSE2 = SMF("Dest Image");
   end = clock();
   CPU_TIME = ((double) (end - start)) / CLOCKS_PER_SEC;
   // Peak Signal to Noise Ratio
   PSNR = 10 * log10(MAXINT/MSE2);
   // MSE1 (orig, noisy), MSE2 (orig, enhanced)
   IEF = MSE1/MSE2;
   RMSE = pow(MSE2, 0.5);
   SSIM = getSSIM();
   printf("RMSE = %.4lf\tPSNR = %.4lf\tSSIM = %lf\tIEF = %.4lf\tTIME = %.2lfs\n", RMSE, PSNR, SSIM, IEF, CPU_TIME);
	}
}
