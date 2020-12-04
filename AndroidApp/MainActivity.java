package com.example.thequalityflow;

import android.os.Bundle;

import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.android.material.snackbar.Snackbar;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;

import android.view.View;

import android.view.Menu;
import android.view.MenuItem;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.ProgressBar;

import org.json.JSONObject;

public class MainActivity extends AppCompatActivity {

    // URL containing json data
    private static final String JSON_URL = "https://api.thingspeak.com/channels/INSERT CHANNEL NUMBER//feeds.json";
    private WebView webView1;
    private WebView webView2;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        /** code for an information button, part of the necessary code was removed from activity_main.
        FloatingActionButton fab = findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.make(view, "Press the button to view statistics about the air quality", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
            }
        });
         */
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
    /**
    private void loadThingSpeakData() {
        //getting the progress bar
        final ProgressBar progressBar = (ProgressBar) findViewById(R.id.progressBar);

        //making progress bar visible
        progressBar.setVisibility(View.VISIBLE);

        //creating a string request to send request to the url
        StringRequest stringRequest = new StringRequest (Request.Method.GET, JSON_URL,
                (response) -> {
                        //hide progress bar when finished with it
                        progressBar.setVisibility(View.INVISIBLE);

                        try{
                            JSONObject obj = new JSONObject(response);
                        }


                })
    }
     */
}
