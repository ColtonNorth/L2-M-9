package com.example.thequalityflow;

import android.os.Build;
import android.os.Bundle;
import android.se.omapi.Channel;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.EditText;

import androidx.annotation.NonNull;
import androidx.annotation.RequiresApi;
import androidx.fragment.app.Fragment;
import androidx.navigation.fragment.NavHostFragment;

import com.android.volley.toolbox.HttpResponse;

import java.io.OutputStream;
import java.util.concurrent.TimeUnit;
import java.io.IOException;
import java.net.HttpURLConnection;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.URL;
import java.net.URLConnection;
import java.nio.charset.StandardCharsets;

public class ThirdFragment extends Fragment {

    private static final String Thingspeak_URL = "https://api.thingspeak.com/update.json?api_key=P2ALDMI1Y8H2Y4JP";
    EditText email;
    WebView DEE;

    @Override
    public View onCreateView(
            LayoutInflater inflater, ViewGroup container,
            Bundle savedInstanceState

    ) {

        // Inflate the layout for this fragment
        View myView1 = inflater.inflate(R.layout.fragment_third, container, false);
        email = (EditText) myView1.findViewById(R.id.userEmail);
        DEE = (WebView) myView1.findViewById(R.id.displayEnteredEmail);
        DEE.setWebViewClient(new WebViewClient());

        return myView1;
    }

    public void onViewCreated(@NonNull View view, Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        view.findViewById(R.id.button_third).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                NavHostFragment.findNavController(ThirdFragment.this)
                        .navigate(R.id.action_ThirdFragment_to_FirstFragment);
            }
        });
        view.findViewById(R.id.submitEmail).setOnClickListener(new View.OnClickListener() {
            @RequiresApi(api = Build.VERSION_CODES.KITKAT)
            @Override
            public void onClick(View view) {
                //Get email entered in EditText, convert to string.
                String em = email.getText().toString();
                String fullURL = Thingspeak_URL.concat("&field2=").concat(em);

                //Best workaround for not having to deal with Java POST bs.
                //Opens a WebView with &field2= to the users entered email.
                DEE.loadUrl(fullURL);
                WebSettings webSettings = DEE.getSettings();
                webSettings.setJavaScriptEnabled(true);
            }
        });
    }
}
