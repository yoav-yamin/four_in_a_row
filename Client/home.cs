using System;
using System.Drawing;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Four_in_a_Row
{
    public partial class home : Form
    {
        private const int NumColumns = 7;
        private const int NumRows = 6; 
        private const int ImageWidth = 450;
        private const int ImageHeight = 350;
        private const int CircleWidth = 54;
        private const int CircleHeight = 50;
        private const int PORT = 65432;
        private int clickedColumn= -1;
        private Graphics g;
        private int player_turn = 0;
        private int row_to_color= -1;
        private int col_to_color= -1;

        public home()
        {
            InitializeComponent();
            StartClientOnClick(this,EventArgs.Empty);
            pictureBox1.MouseClick += LastClickHandler;
        }

        public async void StartClientOnClick(object sender, EventArgs e)
        {
            await Task.Run(() => StartClient());
        }

        public async Task StartClient()
        {
            try
            {
                string[] dataParts;
                TcpClient clientSocket = new TcpClient("127.0.0.1", PORT);
                NetworkStream networkStream = clientSocket.GetStream();
                
                while (true)
                {
                    if (clickedColumn == -1)
                    {
                        continue;
                    }

                    //client data
                    string clientMessage = $"{clickedColumn}";
                    byte[] clientMessageBytes = Encoding.ASCII.GetBytes(clientMessage);
                    await networkStream.WriteAsync(clientMessageBytes, 0, clientMessageBytes.Length);

                    byte[] buffer = new byte[1024];
                    int bytesRead = await networkStream.ReadAsync(buffer, 0, buffer.Length);
                    if (bytesRead == 0)
                        break;
                    string serverData = Encoding.ASCII.GetString(buffer, 0, bytesRead);

                    dataParts = serverData.Split(',');

                    if (dataParts.Length >= 2)
                    {
                        //MessageBox.Show($"Server: {dataParts[0] + "," + dataParts[1]}");
                        Console.WriteLine($"Server: {dataParts[0] + "," + dataParts[1]}");  
                        if (int.TryParse(dataParts[0], out int row) && int.TryParse(dataParts[1], out int col))
                        {
                            row_to_color = row;
                            col_to_color = col;

                            if (col == -1)
                            {
                                MessageBox.Show("This column is full, please pick another column");
                                if (player_turn == 1)
                                {
                                    player_turn = 0;
                                }
                                else
                                {
                                    player_turn = 1;
                                }
                            }

                            if (clickedColumn >= 0 && clickedColumn <= NumColumns)
                            {
                                using (Graphics g = pictureBox1.CreateGraphics())
                                {
                                    int circleX = col_to_color * (ImageWidth / NumColumns) + 5;
                                    int circleY = (NumRows - row_to_color - 1) * (ImageHeight / NumRows) + 5; 
                                    Rectangle circle = new Rectangle(circleX, circleY, CircleWidth, CircleHeight);

                                    if (player_turn == 0)
                                    {
                                        Activate_Redcircle(new PaintEventArgs(g, pictureBox1.ClientRectangle), circle);
                                        player_turn = 1;
                                    }
                                    else
                                    {
                                        Activate_Blackcircle(new PaintEventArgs(g, pictureBox1.ClientRectangle), circle);
                                        player_turn = 0;
                                    }
                                }
                            }
                        }
                        else
                        {
                            Console.WriteLine("Failed to parse row and column from server data.");
                        }
                    }

                    if (dataParts[2] != "")
                    {
                    MessageBox.Show($"Server: {dataParts[2]}");
                    Console.WriteLine(dataParts[2]);
                    string lastclientMessage = $"{dataParts[2]}";
                    byte[] lastclientMessageBytes = Encoding.ASCII.GetBytes(lastclientMessage);
                    await networkStream.WriteAsync(lastclientMessageBytes, 0, lastclientMessageBytes.Length);
                    }
                    clickedColumn = -1;

                }
                clientSocket.Close();
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.ToString());
            }
        }
        private void pictureBox1_Click(object sender, EventArgs e)
        {

        }

        private void LastClickHandler(object sender, MouseEventArgs e)
        {
            clickedColumn = (e.X * NumColumns) / ImageWidth;
        }

        private void Activate_Redcircle(PaintEventArgs e,Rectangle circle)
        {

            e.Graphics.FillEllipse(Brushes.Red, circle);
        }

        private void Activate_Blackcircle(PaintEventArgs e,Rectangle circle)
        {
            e.Graphics.FillEllipse(Brushes.Black, circle);
        }
    }
}
