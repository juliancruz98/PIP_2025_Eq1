int pot = A0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

int valor;
void loop() {
  // put your main code here, to run repeatedly:
  valor = analogRead(pot);
  Serial.println(valor);
  delay(100);

  // E2 IZQ - DER -- punto medio -- DER-IZQ
}
